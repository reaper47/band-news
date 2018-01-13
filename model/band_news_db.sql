SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

DROP SCHEMA IF EXISTS band_news;
CREATE SCHEMA band_news DEFAULT CHARACTER SET utf8;
USE band_news;

-- -----------------------------------------------------
-- Table structure for `location`
-- -----------------------------------------------------
DROP TABLE IF EXISTS location;

CREATE TABLE IF NOT EXISTS location (
    loc_id INT	   UNSIGNED        NOT NULL    AUTO_INCREMENT,
    country        VARCHAR(50)     NOT NULL,
    region         VARCHAR(50)     NOT NULL,
    city           VARCHAR(50)     NOT NULL,
    postal_code    VARCHAR(10)     NOT NULL,
    latitude       DOUBLE UNSIGNED NOT NULL,
    longitude      DOUBLE UNSIGNED NOT NULL,
    metro_code     VARCHAR(10)         NULL,
    area_code      VARCHAR(10)         NULL,
    zip            VARCHAR(10)     NOT NULL,
    name           VARCHAR(50)         NULL,
    street         VARCHAR(100)        NULL,
    PRIMARY KEY (loc_id, city, country, longitude, latitude),
    UNIQUE INDEX id_UNIQUE (loc_id ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table structure for `bands`
-- -----------------------------------------------------
DROP TABLE IF EXISTS bands;

CREATE TABLE IF NOT EXISTS bands (
    band_id    INT UNSIGNED    NOT NULL AUTO_INCREMENT,
    name       VARCHAR(50)     NOT NULL,
    genre      VARCHAR(50)     NOT NULL,
    loc_id     INT UNSIGNED    NOT NULL,
    PRIMARY KEY (band_id, loc_id),
    UNIQUE INDEX id_UNIQUE (band_id ASC),
    INDEX loc_id_idx (loc_id ASC),
    CONSTRAINT loc_id_bands
        FOREIGN KEY (loc_id) 
	REFERENCES band_news.location (loc_id)
    ON DELETE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table structure for `likes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS fb_likes ;

CREATE TABLE IF NOT EXISTS fb_likes (
    fb_likes_id     INT UNSIGNED     NOT NULL AUTO_INCREMENT,
    name            VARCHAR(50)      NOT NULL,
    PRIMARY KEY (fb_likes_id))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table structure for `fb_info`
-- -----------------------------------------------------
DROP TABLE IF EXISTS fb_info ;

CREATE TABLE IF NOT EXISTS fb_info (
  fb_id           INT UNSIGNED     NOT NULL AUTO_INCREMENT,
  about           VARCHAR(3000)    NOT NULL,
  cover           VARCHAR(255)     NOT NULL,
  description     VARCHAR(3000)    NOT NULL,
  fan_count       INT UNSIGNED     NOT NULL,
  fb_likes_id     INT UNSIGNED         NULL,
  PRIMARY KEY (fb_id),
  INDEX likes_id_idx (fb_likes_id ASC),
  CONSTRAINT likes_id_fbinfo
    FOREIGN KEY (fb_likes_id)
    REFERENCES band_news.fb_likes (fb_likes_id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table structure for `events`
-- -----------------------------------------------------
DROP TABLE IF EXISTS events ;

CREATE TABLE IF NOT EXISTS events (
  event_id      INT UNSIGNED     NOT NULL AUTO_INCREMENT,
  ticket_uri    VARCHAR(255)         NULL,
  event_times   DATETIME             NULL,
  start_time    DATETIME         NOT NULL,
  end_time      DATETIME             NULL,
  timezone      VARCHAR(20)      NOT NULL,
  description   VARCHAR(3000)        NULL,
  name          VARCHAR(100)     NOT NULL,
  updated_time  DATETIME         NOT NULL,
  fb_id         INT UNSIGNED     NOT NULL,
  loc_id        INT UNSIGNED     NOT NULL,
  PRIMARY KEY (event_id),
  INDEX fb_id_idx (fb_id ASC),
  INDEX loc_id_idx (loc_id ASC),
  CONSTRAINT fb_id_events
    FOREIGN KEY (fb_id)
    REFERENCES band_news.fb_info (fb_id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT loc_id_events
    FOREIGN KEY (loc_id)
    REFERENCES band_news.location (loc_id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table structure for `fb_post_video_properties`
-- -----------------------------------------------------
DROP TABLE IF EXISTS fb_post_video_properties ;

CREATE TABLE IF NOT EXISTS fb_post_video_properties (
  property_id     INT UNSIGNED     NOT NULL AUTO_INCREMENT,
  name            VARCHAR(50)      NOT NULL,
  text            VARCHAR(50)      NOT NULL,
  PRIMARY KEY (property_id))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table structure for `fb_posts`
-- -----------------------------------------------------
DROP TABLE IF EXISTS fb_posts ;

CREATE TABLE IF NOT EXISTS fb_posts (
  fb_post_id     INT UNSIGNED     NOT NULL AUTO_INCREMENT,
  message        VARCHAR(5000)    NOT NULL,
  full_picture   VARCHAR(255)         NULL,
  properties_id  INT UNSIGNED         NULL,
  source         VARCHAR(255)         NULL,
  permalink_url  VARCHAR(255)     NOT NULL,
  name           VARCHAR(255)     NOT NULL,
  picture        VARCHAR(255)         NULL,
  fb_id          INT UNSIGNED     NOT NULL,
  PRIMARY KEY (fb_post_id),
  INDEX fb_id_idx (fb_id ASC),
  INDEX property_id_idx (properties_id ASC),
  CONSTRAINT fb_id_fbposts
    FOREIGN KEY (fb_id)
    REFERENCES band_news.fb_info (fb_id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT property_id_fbposts
    FOREIGN KEY (properties_id)
    REFERENCES band_news.fb_post_video_properties (property_id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table structure for `fb_photos_album`
-- -----------------------------------------------------
DROP TABLE IF EXISTS fb_photos_album ;

CREATE TABLE IF NOT EXISTS fb_photos_album (
  fb_album_id     INT UNSIGNED     NOT NULL AUTO_INCREMENT,
  created_time    DATETIME         NOT NULL,
  name            VARCHAR(50)      NOT NULL,
  PRIMARY KEY (fb_album_id))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table structure for `fb_photos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS fb_photos ;

CREATE TABLE IF NOT EXISTS fb_photos (
  fb_photo_id     INT UNSIGNED     NOT NULL AUTO_INCREMENT,
  pciture         VARCHAR(255)     NOT NULL,
  fb_album_id     INT UNSIGNED     NOT NULL,
  fb_id           INT UNSIGNED     NOT NULL,
  PRIMARY KEY (fb_photo_id),
  INDEX fb_id_idx (fb_id ASC),
  INDEX fb_album_id_idx (fb_album_id ASC),
  CONSTRAINT fb_id_fbphotos
    FOREIGN KEY (fb_id)
    REFERENCES band_news.fb_info (fb_id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT fb_album_id_fbphotos
    FOREIGN KEY (fb_album_id)
    REFERENCES band_news.fb_photos_album (fb_album_id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table structure for `fb_videos_format`
-- -----------------------------------------------------
DROP TABLE IF EXISTS fb_videos_format ;

CREATE TABLE IF NOT EXISTS fb_videos_format (
  video_format_id     INT UNSIGNED     NOT NULL AUTO_INCREMENT,
  embed_html          VARCHAR(666)     NOT NULL,
  filter              VARCHAR(9)       NOT NULL,
  height              INT              NOT NULL,
  picture             VARCHAR(255)     NOT NULL,
  width               INT              NOT NULL,
  PRIMARY KEY (video_format_id))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table structure for `fb_videos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS fb_videos ;

CREATE TABLE IF NOT EXISTS fb_videos (
  fb_video_id     INT UNSIGNED     NOT NULL AUTO_INCREMENT,
  custom_labels   VARCHAR(50)          NULL,
  format_id       INT UNSIGNED     NOT NULL,
  permalink_url   VARCHAR(255)     NOT NULL,
  title           VARCHAR(100)     NOT NULL,
  source          VARCHAR(255)     NOT NULL,
  description     VARCHAR(2000)        NULL,
  fb_id           INT UNSIGNED     NOT NULL,
  PRIMARY KEY (fb_video_id),
  INDEX fb_id_idx (fb_id ASC),
  INDEX format_id_idx (format_id ASC),
  CONSTRAINT fb_id_fbvideos
    FOREIGN KEY (fb_id)
    REFERENCES band_news.fb_info (fb_id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT format_id_fbvideos
    FOREIGN KEY (format_id)
    REFERENCES band_news.fb_videos_format (video_format_id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table structure for `websites_fb`
-- -----------------------------------------------------
DROP TABLE IF EXISTS websites_fb ;

CREATE TABLE IF NOT EXISTS websites_fb (
  website_fb_id     INT UNSIGNED     NOT NULL AUTO_INCREMENT,
  fb_name           VARCHAR(50)      NOT NULL,
  link              VARCHAR(255)     NOT NULL,
  fb_id             INT UNSIGNED     NOT NULL,
  PRIMARY KEY (website_fb_id),
  INDEX fb_id_idx (fb_id ASC),
  CONSTRAINT fb_id_websitesfb
    FOREIGN KEY (fb_id)
    REFERENCES band_news.fb_info (fb_id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table structure for `websites_official`
-- -----------------------------------------------------
DROP TABLE IF EXISTS websites_official ;

CREATE TABLE IF NOT EXISTS websites_official (
  website_official_id     INT UNSIGNED     NOT NULL AUTO_INCREMENT,
  link                    VARCHAR(255)     NOT NULL,
  PRIMARY KEY (website_official_id))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table structure for `websites`
-- -----------------------------------------------------
DROP TABLE IF EXISTS websites ;

CREATE TABLE IF NOT EXISTS websites (
  website_id              INT UNSIGNED     NOT NULL AUTO_INCREMENT,
  band_id                 INT UNSIGNED     NOT NULL,
  fb_website_id           INT UNSIGNED     NOT NULL,
  official_website_id     INT UNSIGNED     NOT NULL,
  PRIMARY KEY (website_id),
  INDEX band_id_idx (band_id ASC),
  INDEX website_fb_id_idx (fb_website_id ASC),
  INDEX websie_official_id_idx (official_website_id ASC),
  CONSTRAINT band_id_websites
    FOREIGN KEY (band_id)
    REFERENCES band_news.bands (band_id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT website_fb_id_wesbites
    FOREIGN KEY (fb_website_id)
    REFERENCES band_news.websites_fb (website_fb_id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT website_official_id_websites
    FOREIGN KEY (official_website_id)
    REFERENCES band_news.websites_official (website_official_id)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


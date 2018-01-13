import sys
import os
import facebook

dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dir)
import auth

class FbGraph(object):

    def __init__(self):
        auth.store_fb_access_token()
        self.fb_app_info = auth.get_fb_vars()
        
        token = self.fb_app_info['access_token']
        self.graph = facebook.GraphAPI(access_token=token, version='2.7')

        about = 'about'
        cover = 'cover'
        description = 'description'
        events = 'events{ticket_uri,description,event_times,end_time,start_time,name,timezone,updated_time}'
        fans = 'fan_count'
        genre = 'genre'
        likes = 'likes'
        link = 'link'
        posts = 'posts.limit(10){message,full_picture,properties,source,permalink_url,name,picture}'
        photos = 'photos.limit(1){picture,album}'
        videos = 'videos.limit(10){custom_labels,format,permalink_url,title,source,description}'
        website = 'website'

        self.__band_fields = '{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}'.format(
                about, cover, description, events, fans, genre,
                likes, link, posts, photos, videos, website)

    def get_band_info(self, band):
        profile = self.graph.get_object(band)
        info = self.graph.get_object(id=profile['id'], fields=self.__band_fields)
        info['realname'] = profile['name']
        return info



if __name__ == '__main__':
    FbGraph = FbGraph()
    print(FbGraph.get_band_info('sylvaticaofficial'))



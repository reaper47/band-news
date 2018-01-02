import EventEmitter from 'events';


class NavbarStore extends EventEmitter {
  
  constructor() {
    super();

    this.showMenu = false;
  }

  getShowMenu() {
    return this.showMenu;
  }

  toggleShowMenu() {
    this.showMenu = !this.showMenu;
    this.updateMenu();
  }

  updateMenu() {
    this.emit('update_menu', this.showMenu);
  }

}

export default NavbarStore;

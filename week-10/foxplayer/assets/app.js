'use strcit';

class App {
    constructor(){
        const myPanel = controlPanel();
        const myPlayLists = playLists();
        const myTrackList = trackList();

        myTrackList.firstHandler(myPanel.playTrack);
        myTrackList.load();

        myTrackList.clickHandler(myPanel.playTrack);
    }
}

const application = new App();
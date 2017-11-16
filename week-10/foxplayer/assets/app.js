'use strcit';

class App {
    constructor(){
        const myPanel = controlPanel();
        const myTrackInfo = trackInfo();
        const myPlayLists = playLists();
        const myTrackList = trackList();

        myPlayLists.load();
        myPlayLists.clickHandler(myTrackList.load);
        myTrackList.firstHandler([myPanel.playTrack, myTrackInfo.display]);
        myTrackList.load();

        myTrackList.clickHandler([myPanel.playTrack, myTrackInfo.display]);
        myPanel.nextBtnPressed(myTrackList.playNext);
        myPanel.prevBtnPressed(myTrackList.playPrev);
    }
}

const application = new App();
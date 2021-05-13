function loadSTL(){

    // loads the stl viewer
    stl_viewer = new StlViewer(document.getElementById("stl_cont"), {
        auto_rotate: true,
        models: [{
            id:0, 
            filename:"/stlfile.stl",
            rotationx: -1.5,
            rotationz: 0.5
        }]
    });

    setTimeout(function () {

        // removes the loading text
        var stlDiv = document.getElementById('loading')
        stlDiv.style.display = 'none'

    // timeout 1000ms
    }, 950);
}

function constantPlay(){
    if (constantRotate == false){
        constantRotate = true
        play()
    }
    else{
        constantRotate = false
        pause()
    }
}

function pause(){
    if (constantRotate == false){
        stl_viewer.animate_model(0, {delta:{rotationz:0, msec:1500, loop:true}} );
    }
}

function play(){
    stl_viewer.animate_model(0, {delta:{rotationz:1.2, msec:1500, loop:true}} );
}

var constantRotate = false
var stl_viewer;

function loadSTL(file){

	document.getElementById('stlViewer').style.display = 'block'
	container = document.getElementById('stlContainer')
	container.innerHTML = null
	// loads the stl viewer
	stl_viewer = new StlViewer(container, {
		auto_rotate: true,
		models: [{
			id:0, 
			filename: file,
			rotationy: Math.PI * 5/4,
		}]
	});
}
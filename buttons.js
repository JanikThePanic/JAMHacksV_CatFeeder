cadButton = document.getElementById('cadButton')
codeButton = document.getElementById('codeButton')

function showCad(){
	cadButton.style.backgroundColor = 'rgb(153,153,25)'
	codeButton.style.backgroundColor = 'rgb(50,50,50)'
	document.getElementById('stlViewer').style.display = 'block'
	loadSTL()
}

function closeCad(){
	cadButton.style.backgroundColor = 'rgb(50,50,50)'
	document.getElementById('stlViewer').style.display = 'none'
}

function showCode(){
	codeButton.style.backgroundColor = 'rgb(153,153,25)'
	cadButton.style.backgroundColor = 'rgb(50,50,50)'
}
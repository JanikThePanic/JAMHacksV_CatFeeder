cadButton = document.getElementById('cadButton')
codeButton = document.getElementById('codeButton')
showcaseButton = document.getElementById('showcaseButton')

function showCad(){
	clearButtons()
	clearContent()
	document.getElementById('cadList').style.display = 'flex'
	cadButton.style.backgroundColor = 'purple'
}

function showCode(){
	clearButtons()
	clearContent()
	document.getElementById('codeList').style.display = 'flex'
	codeButton.style.backgroundColor = 'purple'
}

function showVideo(){
	clearButtons()
	clearContent()
	document.getElementById('video').style.display='block'
	showcaseButton.style.backgroundColor = 'purple'
}

function closeCad(){
	document.getElementById('stlViewer').style.display = 'none'
}

function clearContent(){
	document.getElementById('codeList').style.display = 'none'
	document.getElementById('cadList').style.display = 'none'
	document.getElementById('video').style.display = 'none'
}

function clearButtons(){
	codeButton.style.backgroundColor = 'rgb(50,50,50)'
	cadButton.style.backgroundColor = 'rgb(50,50,50)'
	showcaseButton.style.backgroundColor = 'rgb(50,50,50)'
}
cadButton = document.getElementById('cadButton')
codeButton = document.getElementById('codeButton')
showcaseButton = document.getElementById('showcaseButton')

function showCad(){
	clearButtons()
	clearContent()
	document.getElementById('cadList').style.display = 'flex'
	cadButton.style.backgroundColor = 'rgb(153,153,25)'
}

function showCode(){
	clearButtons()
	clearContent()
	document.getElementById('codeList').style.display = 'flex'
	codeButton.style.backgroundColor = 'rgb(153,153,25)'
}

function showVideo(){
	clearButtons()
	clearContent()
	showcaseButton.style.backgroundColor = 'rgb(153,153,25)'
}

function closeCad(){
	clearButtons()
	document.getElementById('stlViewer').style.display = 'none'
}

function clearContent(){
	document.getElementById('codeList').style.display = 'none'
	document.getElementById('cadList').style.display = 'none'
}

function clearButtons(){
	codeButton.style.backgroundColor = 'rgb(50,50,50)'
	cadButton.style.backgroundColor = 'rgb(50,50,50)'
	showcaseButton.style.backgroundColor = 'rgb(50,50,50)'
}
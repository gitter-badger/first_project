// files
function button_1() {
	hiddenDiv = document.getElementById('fileHidden'); 
	fButton = document.getElementById('fButton'); 
	if (hiddenDiv.style.display == 'none') {
		hiddenDiv.style.display = 'block'; 
		fButton.firstChild.data = 'Hide files fields'; 
	} 
	else { 
		hiddenDiv.style.display = 'none'; 
		fButton.firstChild.data = 'Show files fields'; 
	} 
}
var l = 1;
function add_element(container){
	l = l + 1;
	var znacznik = document.createElement('input');
	znacznik.setAttribute('type', 'file');
	znacznik.setAttribute('name', 'file');
	znacznik.setAttribute('id', 'inputFile' + l);
	znacznik.className = 'upload';
	var container = document.getElementById(container);
	container.appendChild(znacznik);
	document.getElementById('removeButton').style.display = 'block';
	if(l==10) {
		document.getElementById('addButton').style.display = 'none';
		return;
	}
}
function remove_element(container){
	document.getElementById('addButton').style.display = 'block';
	var container = document.getElementById(container);
	var child = document.getElementById('inputFile' + l);
	container.removeChild(child);
	if(l==2) {
		document.getElementById('removeButton').style.display = 'none';
		l = l - 1;
		return;
	}
	l = l - 1;
}

// gifts
function button_2() {
	hiddenDiv = document.getElementById('giftHidden'); 
	gButton = document.getElementById('gButton'); 
	if (hiddenDiv.style.display == 'none') { 
		hiddenDiv.style.display = 'block'; 
		gButton.firstChild.data = 'Hide gifts fields'; 
	} 
	else { 
		hiddenDiv.style.display = 'none'; 
		gButton.firstChild.data = 'Show gifts fields';
	} 
}
var i = 1;
function show_element_2(container,hider,name){
	i = i + 1;
	document.getElementById(hider).style.display = 'block';
	element = document.getElementById('' + name + i);
	element.style.display = 'block';
	if(i==10) {
		document.getElementById(container).style.display = 'none';
		return;
	}
}
function hide_element_2(container,shower,name){
	document.getElementById(shower).style.display = 'block';
	element = document.getElementById('' + name + i);
	element.style.display = 'none';
	if(i==2) {
		document.getElementById(container).style.display = 'none';
		i = i - 1;
		return;
	}
	i = i - 1;
}

// small events
function button_3() {
	hiddenDiv = document.getElementById('smallEventsHidden'); 
	seButton = document.getElementById('seButton'); 
	if (hiddenDiv.style.display == 'none') { 
		hiddenDiv.style.display = 'block'; 
		seButton.firstChild.data = 'Hide small events fields'; 
	} 
	else { 
		hiddenDiv.style.display = 'none'; 
		seButton.firstChild.data = 'Show small events fields'; 
	} 
}
var j = 1;
function show_element_3(container,hider,name){
	j = j + 1;
	document.getElementById(hider).style.display = 'block';
	element = document.getElementById('' + name + j);
	element.style.display = 'block';
	if(j==10) {
		document.getElementById(container).style.display = 'none';
		return;
	}
}
function hide_element_3(container,shower,name){
	document.getElementById(shower).style.display = 'block';
	element = document.getElementById('' + name + j);
	element.style.display = 'none';
	if(j==2) {
		document.getElementById(container).style.display = 'none';
		j = j - 1;
		return;
	}
	j = j - 1;
}

// own fields
function button_4() {
	hiddenDiv = document.getElementById('addOwnFieldsHidden'); 
	addButton = document.getElementById('addButton'); 
	if (hiddenDiv.style.display == 'none') { 
		hiddenDiv.style.display = 'block'; 
		addButton.firstChild.data = 'Hide panel of adding your own fields'; 
	} 
	else { 
		hiddenDiv.style.display = 'none'; 
		addButton.firstChild.data = 'Show panel of adding your own fields'; 
	} 
}
var k = 1;
function show_element_4(container,hider,name){
	k = k + 1;
	document.getElementById(hider).style.display = 'block';
	element = document.getElementById('' + name + k);
	element.style.display = 'block';
	if(k==10) {
		document.getElementById(container).style.display = 'none';
		return;
	}
}
function hide_element_4(container,shower,name){
	document.getElementById(shower).style.display = 'block';
	element = document.getElementById('' + name + k);
	element.style.display = 'none';
	if(k==2) {
		document.getElementById(container).style.display = 'none';
		k = k - 1;
		return;
	}
	k = k - 1;
}
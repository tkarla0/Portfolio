function calPerimeter(len,wid){
  var perimeter = 2 * (len + wid)
  return perimeter ;
}

function calArea(length , width){

  return length * width;
}

function btnCalculate_onclick(){
var lengthText = document.getElementById("txtLength");
	var widthText = document.getElementById("txtWidth");
	var areaText = document.getElementById("txtArea");
	var perimeterText = document.getElementById("txtPerimeter");

var length = parseFloat(lengthText.value);
  var width = parseFloat(widthText.value);

var area = calArea(length , width);
  var perimeter = calPerimeter(length , width);

areaText.value = area;
perimeterText.value = perimeter
}
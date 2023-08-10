function btnDisplay_onclick()
{
	// get textboxes and assign to variables
	var ageTextbox = document.getElementById("txtAge");
	var minWeightTextbox = document.getElementById("txtWeightMin");
	var maxWeightTextbox = document.getElementById("txtWeightMax");
	var minHeightTexbox = document.getElementById("txtHeightMin");
	var maxHeightTexbox = document.getElementById("txtHeightMax");
	
	var minWeight = new Array(5,15,25,45,60,65,70,75,80);
	var maxWeight = new Array (8,30,45,65,85,100,110,120,125);
	var minHeight = new Array(10,13,17,20,24,26,27,28,28);
	var maxHeight = new Array(13,18,23,25,30,33,34,34,35);
	
	var ageValue = ageTextbox.value ; 
	 var indexNumber = ageValue- 1 ; 
  if (ageValue > 9 || ageValue === 0 || Number.isInteger(ageValue) === false ){
    minWeightTextbox.value = "Invalid Input ,Please enter a number between 1-9"
maxWeightTextbox.value = "Invalid Input ,Please enter a number between 1-9"
minHeightTexbox.value = "Invalid Input ,Please enter a number between 1-9"
maxHeightTexbox.value = "Invalid Input ,Please enter a number between 1-9"
  } else {
    minWeightTextbox.value = minWeight[indexNumber];
maxWeightTextbox.value = maxWeight[indexNumber];
minHeightTexbox.value = minHeight[indexNumber];
maxHeightTexbox.value = maxHeight[indexNumber];
  }

}
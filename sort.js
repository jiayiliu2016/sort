function insertionSort(arr) {
    var len = arr.length;
    var preIndex, current;
    for (var i = 1; i < len; i++) {
        preIndex = i - 1;
        current = arr[i];
        while(preIndex >= 0 && arr[preIndex] > current) {
            arr[preIndex+1] = arr[preIndex];
            preIndex--;
        }
        arr[preIndex+1] = current;
    }
    return arr;
}


function insertionSort(arr){
    var len=arr.length;
    var preIndex, current;
        for (var i=1; i<length; i++){
            preIndex= i-1;
            current=a[i];
            whlie(preIndex>=0 && current<arr[preIndex]){
                
                preIndex--;
            }

        }
}

function shellinsort(arr){
    var len=arr.length,temp,gap=1;
    while(gap<len/3){
        gap=gap*3+1;
    }

}
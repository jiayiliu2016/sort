/*  feature:   直接选择排序的改进版
	编号为i的节点：
	    1\ 双亲编号为 i/2
	    2、若2i<n, ki左孩子节点为2i； 否则ki为叶子
	    3、若2i+1<=n，ki的右孩子节点为2i+1； 否则ki无右孩子节点

	从最后一个非叶子节点i开始，将以i为根节点的二叉树调整为堆 （目标：所有的子树都为堆的完全二叉树）
 */


/*
    输入：数组A，堆的长度hLen，以及需要调整的节点i
    功能：调堆
 */
void AdjustHeap(int A[], int hLen, int i){
	// int left=LeftChild(i);
	// int right=RightChild(i);
	int largest=i;
	int temp;

	while(left<hLen || right<hLen){
		if(left<hLen && A[largest]<A[left]){
			largest=left;
		}
		if(right<hLen && A[largest]<A[right]){
			largest=right;
		}

		if(i!=largest){              //father-node is not the max
			temp=A[largest];
			A[largest]=A[i];
			A[i]=temp;

			i=largest;
			left=LeftChild(i);
			right=RightChild(i);
		}
		else{
			break;
		}
	}
}

void BuildHeap(int A[], int aLen){
	int i;
	int begin=hLen/2-1;        // last non-leafnode
	for(i=begin; i>=0; i--){
		AdjustHeap(A, hLen, i);
	}
}

void Heapsort(int A[], int aLen){
	int hLen=aLen;
	int temp;

	BuildHeap(A, hLen);        // set heap

	while(hLen>1){
		temp=A[hLen-1];       // exchange A[0] and A[hLen]
		A[hLen-1]=A[0];
		A[0]=temp;
		hLen--;            // size of heap -1
		AdjustHeap(A,hLen,0);
	}
}





// package sort;
 
// import java.util.Arrays;
// import util.MathUtil;
// /**
//  * 通过大顶堆实现堆排序，升序排序
//  * 
//  */
 
// public class HeapSort {
//     public static void main(String[] args) {
//         int[] arr={9,6,12,32,23,11,2,100,85};
//         sort(arr);
//         System.out.println(Arrays.toString(arr));
//     }
//     //这里将i定义为完全二叉树的根
//     //将完全二叉树调整为大顶堆,前提是二叉树的根的子树已经为大顶堆。
//     public static void adjustHeap(int[]a ,int i,int size){
//         int lChild=2*i+1;        //左孩子
//         int rChild=2*i+2;        //又孩子
//         int max=i;                //临时变量
//         if(i<size/2){            //如果i是叶子节点就结束
//             if(lChild<size&&a[max]<a[lChild])
//                 max=lChild;
//             if(rChild<size&&a[max]<a[rChild])
//                 max=rChild;
//             if(max!=i){
//                 MathUtil.swap(a, max, i);//交换后破环了子树的堆结构
//                 adjustHeap(a, max, size);//递归，调节子树为堆
//             }
//         }
//     }
     
//     //建立堆，堆是从下往上建立的，因为adjustHeap函数是建立在子树已经为大顶堆。
//     public static void buildHeap(int[]a,int size){    
//         for(int i=size/2;i>=0;i--){//从最后一个非叶子节点，才能构成adjustHeap操作的目标二叉树
//             adjustHeap(a, i, size);
//         }        
//     }
 
//     //将数组分为两部分，一部分为有序区，在数组末尾，另一部分为无序区。堆属于无序区
//     public static void sort(int[] arr){
//         int size=arr.length;
//         buildHeap(arr, size);
//         for(int i=size-1;i>0;i--){//i为无序区的长度，经过如下两步，长度递减
//             //堆顶即下标为0的元素
//             MathUtil.swap(arr, i, 0);//1.每次将堆顶元素和无序区最后一个元素交换，即将无序区最大的元素放入有序区
//             adjustHeap(arr, 0, i);   //2.将无顺区调整为大顶堆，即选择出最大的元素。
//         }
//     }    
// }



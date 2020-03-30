#include <stdio.h>
#include <stdlib.h>
int* sortArray(int* nums, int numsSize, int* returnSize);

int main()
{
    int nums[6] = {6,5,4,3,7,1};
    int Size = 0;
    int *result = sortArray(nums,6,&Size);
    for(int i = 0;i<Size;i++){
        printf("%d ",result[i]);
    }
    return 0;
}

int* sortArray(int* nums, int numsSize, int* returnSize){
    BubbleSort(nums,numsSize);
    *returnSize = numsSize;
    return nums;
}

//堆排序----------------------------------------------------------
void BigHeadAdjust(int *arr,int index,int length)
{
	int lchild = 2 * index + 1;
	int rchild = 2 * index + 2;
	int max = index;
	if (lchild<length&&arr[lchild]>arr[max])
	{
		max = lchild;
	}
	if (rchild<length&&arr[rchild]>arr[max])
	{
		max = rchild;
	}
	if (max != index)
	{
		Swap(&arr[max], &arr[index]);
		BigHeadAdjust(arr, max, length);
	}
	return;
}

//堆排序，采用大顶堆 升序
void HeapSort_Up(int *arr, int length)
{
	//初始化堆，将每个非叶子结点倒叙进行大顶堆调整。
	//循环完毕 初始大顶堆（每个根结点都比它孩子结点值大）形成
	for (int i = length / 2 - 1; i >= 0; i--)
	{
		BigHeadAdjust(arr, i, length);
	}
	//printf("大堆顶初始化顺序：");
	//将堆顶值放到数组尾部，然后又进行大堆顶调整，一次堆调整最值就到堆顶了。
	for (int i = length - 1; i >= 0; i--)
	{
		Swap(&arr[0], &arr[i]);
		BigHeadAdjust(arr, 0, i);
	}
	return;
}

void Swap(int* a, int* b)
{
	int temp = *a;
	*a = *b;
	*b = temp;
}
//堆排序----------------------------------------------------------

/*-------------------------------------------------------------------------------*/

//快速排序-----------------------------------------------------------
void QuickSort(int *a,int left,int right)
{
    int i,j,temp,temp1;
    i=left;
    j=right;
    temp=a[left];
    if(left>right)
        return;
    while(i!=j)
    {
        while(a[j]>=temp && j>i)
            j--;
        if(j>i){
            a[i++]=a[j];

        }
        while(a[i] <=temp && j>i)
            i++;
        if(j>i){
            a[j--]=a[i];
        }
    }
    a[i]=temp;
    QuickSort(a,left,i-1);
    QuickSort(a,i+1,right);
}
//快速排序-----------------------------------------------------------

/*-------------------------------------------------------------------------------*/

//冒泡排序-----------------------------------------------------------
void BubbleSort(int *a,int Size){
    int i,j,temp=0;
    for(i=0;i<Size;i++){
        for(j=0;j<Size-i-1;j++){
            if(a[j]>a[j+1]){
                temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
            }
        }
    }
}

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int nums[7] = {2,2,1,1,1,2,2};
    int result = majorityElement(nums,7);
    printf("%d",result);
    return 0;
}

int majorityElement(int* nums, int numsSize){
    int index;
    HeapSort_Up(nums,numsSize);
    index = numsSize/2;
    return nums[index];
}


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
	//PrintArr(arr, length);
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

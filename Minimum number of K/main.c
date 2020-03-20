#include <stdio.h>
#include <stdlib.h>

int* getLeastNumbers(int* arr, int arrSize, int k, int* returnSize);

int main()
{
    int arr[10] = {5,7,9,10,8,3,2,0,1,11};
    int k = 3;
    int Size = 0;
    int *result = getLeastNumbers(arr,10,k,&Size);
    for(int i=0;i<Size;i++)
        printf("%d ",result[i]);
    free(result);
    return 0;
}


int* getLeastNumbers(int* arr, int arrSize, int k, int* returnSize){
    int i,j,temp;
    /*for(i=0;i<arrSize;i++){
        for(j=0;j<arrSize-i-1;j++){
            if(arr[j]>arr[j+1]){
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }           冒泡会超时*/
    HeapSort_Up(arr,arrSize);  //堆排序不会超时
    int *ans;
    ans = (int *)calloc(k,sizeof(int));
    for(i=0;i<k;i++)
        ans[i] = arr[i];
    *returnSize = k;
    return ans;
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

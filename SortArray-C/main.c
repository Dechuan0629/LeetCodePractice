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

//������----------------------------------------------------------
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

//�����򣬲��ô󶥶� ����
void HeapSort_Up(int *arr, int length)
{
	//��ʼ���ѣ���ÿ����Ҷ�ӽ�㵹����д󶥶ѵ�����
	//ѭ����� ��ʼ�󶥶ѣ�ÿ������㶼�������ӽ��ֵ���γ�
	for (int i = length / 2 - 1; i >= 0; i--)
	{
		BigHeadAdjust(arr, i, length);
	}
	//printf("��Ѷ���ʼ��˳��");
	//���Ѷ�ֵ�ŵ�����β����Ȼ���ֽ��д�Ѷ�������һ�ζѵ�����ֵ�͵��Ѷ��ˡ�
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
//������----------------------------------------------------------

/*-------------------------------------------------------------------------------*/

//��������-----------------------------------------------------------
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
//��������-----------------------------------------------------------

/*-------------------------------------------------------------------------------*/

//ð������-----------------------------------------------------------
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

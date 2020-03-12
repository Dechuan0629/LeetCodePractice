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
	//PrintArr(arr, length);
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

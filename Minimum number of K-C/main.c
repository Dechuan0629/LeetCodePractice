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
    }           ð�ݻᳬʱ*/
    HeapSort_Up(arr,arrSize);  //�����򲻻ᳬʱ
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

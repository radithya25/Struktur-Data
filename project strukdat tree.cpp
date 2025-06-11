#include <iostream>

using namespace std;

struct node{
	int data;
	node* kiri;
	node* kanan;
};

node* buatnode(int data){
	node* nodebaru = new node();
	nodebaru->data = data;
	nodebaru->kiri = NULL;
	nodebaru->kanan = NULL;
	return nodebaru;
}

node* tambah(node*root, int data){
	if(root==NULL){
		return buatnode(data);
	}
	if(data < root->data){
		root->kiri = tambah(root->kiri, data);
	}else if (data > root -> data){
		root-> kanan = tambah(root->kanan, data);
	}
	return root;
}

void preorder(node* root){
	if (root !=NULL){
		cout<< root->data<<" ";
		preorder(root->kiri);
		preorder(root->kanan);
	}
}

void inorder(node* root){
	if (root !=NULL){
		inorder(root->kiri);
		cout<< root->data<<" ";
		inorder(root->kanan);
	}
}

void postorder(node* root){
	if (root !=NULL){
		postorder(root->kiri);
		postorder(root->kanan);
		cout<< root->data<<" ";
	}
}

int main() {
	node* root = NULL;
	int pilihan, data;
	
	do{
		system("cls");
		cout << "\n===== PROGRAM BINARY TREE =====";
		cout << "\n1. Tambah data";
		cout << "\n2. Tampilkan PreOrder";
		cout << "\n3. Tampilkan InOrder";
		cout << "\n4. Tampilkan PostOrder";
		cout << "\n5. Keluar";
		cout << "\nPilihan Anda: ";
		cin >> pilihan;
		
		system("cls");
		switch(pilihan){
			case 1:
				cout << " Masukkan data: ";
				cin >> data;
				root = tambah(root, data);
				cout << "Data berhasil ditambahkan\n";
				break;
			case 2:
				cout << "Tampilan secara PreOrder: ";
				preorder(root);
				cout<< endl;
				break;
			case 3:
				cout << "Tampilan secara InOrder: ";
				inorder(root);
				cout<< endl;
				break;
			case 4:
				cout << "Tampilan secara PostOrder: ";
				postorder(root);
				cout<< endl;
				break;
			case 5:
				cout<< "keluar dari program..";
				break;
			default:
				cout<< "Pilihan tidak valid!";		 
		}	
		system("pause");
	} while (pilihan !=5);
	
	return 0;
}

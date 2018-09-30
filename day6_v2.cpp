/*
* @Author: VU Anh Tuan
* @Date:   2018-09-30 09:22:59
* @Last Modified by:   VU Anh Tuan
* @Last Modified time: 2018-09-30 14:26:34
*/

#include <iostream>
using namespace std;

#include <stdio.h> 
#include <stdlib.h> 
#include <inttypes.h>

struct Element{
	int val;
	Element *both;
};

Element *XOR(struct Element *a, struct Element *b){
	return (struct Element*)((uintptr_t)(a) ^ (uintptr_t)(b));
}

class LinkedList{
protected:
	Element *head;
	Element *tail;
public:
	LinkedList(){
		this->head = NULL;
	}

	Element *get_ele(Element *prev_next, Element *cur){
		return XOR(prev_next, cur->both);
	}

	void add(int val){
		Element *ele = new Element;
		ele->val = val;
		ele->both = NULL;
		cout << "add(" << val << ")\n";

		if (this->head == NULL){
			this->head = ele;
			this->tail = ele;
		} else{
			ele->both = XOR(this->tail, NULL);
			this->tail->both = XOR(this->tail->both, ele);
			this->tail = ele;
		}
	}

	Element *get(int index){
		if (this->head == NULL) return NULL;
		if (index >= 0){ // from head to tail
			Element *prev = NULL;
			Element *cur = this->head;
			int i = 0;
			Element *next = this->get_ele(prev, cur);
			while ((next != NULL) && (i < index)){
				prev = cur; cur = next;
				next = this->get_ele(prev, cur);
				i++;
			}
			if (i==index) return cur;
			else return NULL;
		}
		if (index < 0){ // from tail to head
			Element *next = NULL;
			Element *cur = this->tail;
			int i = -1;
			Element *prev = this->get_ele(next, cur);
			while((prev != NULL) && (i > index)){
				next = cur; cur = prev;
				prev = this->get_ele(next, cur);
				i--;
			}
			if (i==index) return cur;
			else return NULL;
		}
	}

	void print(){
		if (this->head == NULL) return;
		Element *prev = NULL;
		Element *cur = this->head;
		cout << cur->val << " ";
		Element *next = this->get_ele(prev, cur);
		while(next != NULL){
			prev = cur;
			cur = next;
			cout << cur->val << " ";
			next = this->get_ele(prev, cur);
		}
		cout << "\n";
	}
};

int main(){
	LinkedList *ll = new LinkedList;
	ll->add(3); ll->add(5); ll->add(7); ll->add(9);	
	cout << "List: ";
	ll->print();

	int index[] = {0, -1, 1};
	Element *ele;
	for (int i = 0; i < 3; i++){
		ele = ll->get(index[i]);
		cout << "get(" << index[i] << ") = ";
		if (ele != NULL) cout << ele->val << "\n";
		else  cout << "NULL\n";
	}

	return 0;
}
/*
* @Author: VU Anh Tuan
* @Date:   2018-09-26 05:41:53
* @Last Modified by:   VU Anh Tuan
* @Last Modified time: 2018-09-29 18:08:24
*/

/*
* This problem was asked by Google.
* An XOR linked list is a more memory efficient doubly linked list.
* Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node.
* Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.
* If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions 
* that converts between nodes and memory addresses.
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
public:
	LinkedList(){
		this->head = NULL;
	}

	Element *get_next(Element *prev, Element *both){
		return XOR(prev, both);
	}

	void add(int val){
		Element *ele = new Element;
		ele->val = val;
		ele->both = NULL;
		cout << "add(" << val << ")\n";

		if (this->head == NULL){
			this->head = ele;
		} else{
			ele->both = XOR(NULL, this->head);
			this->head->both = XOR(ele, this->head->both);
			this->head = ele;
		}
	}

	Element *get(int index){
		if (this->head == NULL) return NULL;
		Element* prev = NULL;
		Element* cur = this->head;
		int i = 1;
		Element *next = this->get_next(prev, cur->both);
		while ((next != NULL) && (i < index)){
			prev = cur;
			cur = next;
			next = this->get_next(prev, cur->both);
			i++;
		}
		if (i==index){
			return cur;
		} else{
			return NULL;
		}
	}

	void print(){
		if (this->head == NULL) return;
		Element *prev = NULL;
		Element *cur = this->head;
		cout << cur->val << " ";
		Element *next = this->get_next(prev, cur->both);
		while(next != NULL){
			prev = cur;
			cur = next;
			cout << cur->val << " ";
			next = this->get_next(prev, cur->both);
		}
		cout << "\n";
	}
};

int main(){
	LinkedList *ll = new LinkedList;
	ll->add(3); ll->add(5); ll->add(7); ll->add(9);
	cout << "List: ";
	ll->print();

	int index = 2;
	Element *ele = ll->get(index);
	cout << "get(" << index << ") = ";
	if (ele != NULL){
		cout << ele->val << "\n";
	} else {
		cout << "NULL\n";
	}
	return 0;
}
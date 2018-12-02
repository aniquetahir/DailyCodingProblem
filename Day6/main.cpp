#include <cstdlib>
#include <iostream>

struct XORLinkedListElement{
        int value;
        uintptr_t both;
};

class XORLinkedList {
    private:
        XORLinkedListElement* start;
        XORLinkedListElement* end;

    public:
        XORLinkedList(){
            start = nullptr;
            end = nullptr;
        }

        void add(int element){
            XORLinkedListElement* newElement = (XORLinkedListElement*)malloc(sizeof(XORLinkedListElement));
            *(&newElement->value) = element;
            *(&newElement->both) = (uintptr_t) nullptr ^ (uintptr_t) nullptr;

            if(start == nullptr){
                start = newElement;
                end = newElement;
            }else{
                XORLinkedListElement* previous_element = end;
                previous_element->both = (uintptr_t)newElement ^ (previous_element->both ^ (uintptr_t)nullptr);
                newElement->both = (uintptr_t)nullptr ^ (uintptr_t)previous_element;
                end = newElement;
            }
        }

        int get(int index){
            int curr_index = 0;
            XORLinkedListElement* curr_element = start;
            XORLinkedListElement* prev_element = nullptr;

            while(curr_index!=index){
                uintptr_t next_element_address = curr_element->both ^ (uintptr_t)prev_element;
                prev_element = curr_element;
                curr_element = (XORLinkedListElement*)next_element_address;
                curr_index += 1;
            }

            return curr_element->value;
        }

};

void test(){
    XORLinkedList list = XORLinkedList();
    list.add(9);
    list.add(2);
    list.add(3);
    list.add(6);

    assert(list.get(0) == 9);
    assert(list.get(1) == 2);
    assert(list.get(2) == 3);
    assert(list.get(3) == 6);
}

int main(){
    test();
    return 0;
}

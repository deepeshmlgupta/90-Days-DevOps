#include <iostream>

struct Node {
    int data;
    Node* next;
    Node(int value) : data(value), next(nullptr) {}
};

Node* reverse(Node* temp) {
    if (temp == nullptr || temp->next == nullptr)
        return temp;

    Node* reversed_list = reverse(temp->next); // Step 2

    // Adjust pointers to reverse the direction
    temp->next->next = temp;
    temp->next = nullptr;

    return reversed_list;
}

void printList(Node* head) {
    while (head != nullptr) {
        std::cout << head->data << " ";
        head = head->next;
    }
    std::cout << std::endl;
}

int main() {
    // Example usage
    Node* head = new Node(1);
    head->next = new Node(2);
    head->next->next = new Node(3);
    head->next->next->next = new Node(4);

    std::cout << "Original list: ";
    printList(head);

    head = reverse(head);

    std::cout << "Reversed list: ";
    printList(head);

    return 0;
}

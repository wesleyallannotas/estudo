package util;

public class Node<T> {
    // Atributos
    private T value;
    private Node<T> next;      // Definição recursiva, ponteiro

    // Getters e Setters
    public T getValue() {
        return value;
    }
    public void setValue(T value) {
        this.value = value;
    }
    public Node<T> getNext() {
        return next;
    }
    public void setNext(Node<T> next) {
        this.next = next;
    }
}
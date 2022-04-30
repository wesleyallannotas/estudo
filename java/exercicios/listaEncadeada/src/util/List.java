package util;

public class List<T> {
    // Atributos
    private Node<T> head;

    // Métodos
    public void add(T value) {     // Inserindo sempre no inicio.
        Node<T> node = new Node<>();
        node.setValue(value);
        node.setNext(head);
        head = node;      
    }
    
    @Override
    public String toString() {
        StringBuffer sb = new StringBuffer();
        
        sb.append("[ ");
        
        Node<T> p = head;
        while(p != null) {
            sb.append(p.getValue() + " ");
            p = p.getNext();
        }
        
        sb.append("]");
        return sb.toString();
    }
}
# Liskov Substitution Principle
### an object and a sub-object must be interchangeable without breaking the program.
> When extending a class, remember that you should be able to pass objects of the subclass <br>
> in place of objects of the parent class without breaking the client code.

### Example
Rectangle Class
```java
class Rectangle {
    private int width;
    private int height;

    public void setHeight(int height) {
        this.height = height;
    }

    public int getHeight() {
        return this.height;
    }

    public void setWidth(int width) {
        this.width = width;
    }

    public int getWidth() {
        return this.width;
    }

    public int area() {
        return this.width * this.height;
    }
}
```
Square Class
```java
class Square extends Rectangle {
    @Override
    public void setHeight(int value) {
        this.width = value;
        this.height = value;
    }

    @Override
    public void setWidth(int value) {
        this.width = value;
        this.height = value;
    }
}
```
TestLSP Class
```
class TestLSP {
    static boolean checkAreaSize(Rectangle r) {
        r.setWidth(5);
        r.setHeight(4);

        if(r.area() != 20 ){ // Error Size
            return false;
        }

        return true;
    }
    public static void main(String[] args){
        Test.checkAreaSize(new Rectangle()); // true
        Test.checkAreaSize(new Square()); // false
    }
}
```
### 해결 방법
상속 관계 제거

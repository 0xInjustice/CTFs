[General Skills](https://play.picoctf.org/practice/challenge/462)

# Description
The Rust saga continues? I ask you, can I borrow that, pleeeeeaaaasseeeee?

# Solution

# Error

- `error[E0596]: cannot borrow `*borrowed_string` as mutable, as it is behind a `&` reference`

```rust
fn decrypt(encrypted_buffer:Vec<u8>, borrowed_string: &mut String){ // How do we pass values to a function that we want to change?


    let mut party_foul = String::from("Using memory unsafe languages is a: "); // Is this variable changeable?
    decrypt(encrypted_buffer, &mut party_foul); // Is this the correct way to pass a value to a function so that it can be changed?
```

> changed dycrypt functioin argument `borrowed_string` to ``&mut Strings`` and make the according changes related to the error `E0596`

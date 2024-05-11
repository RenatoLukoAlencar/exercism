pub fn reverse(input: &str) -> String {
    let mut new_str: String = "".to_owned();

    for character in input.chars() {
        new_str = format!("{character}{new_str}")
    }

    return new_str;
}

use regex::Regex;
use std::{
    error::Error,
    fs::File,
    io::{BufRead, BufReader},
};

fn create_file_reader(fpath: &str) -> Result<BufReader<File>, Box<dyn Error>> {
    let file = File::open(fpath)?;

    Ok(BufReader::new(file))
}

fn find_capture_products(pattern: &Regex, content: &str) -> isize {
    let mut solution: isize = 0;

    for capture in pattern.captures_iter(&content) {
        let num1: isize = capture.get(1).unwrap().as_str().parse().unwrap();
        let num2: isize = capture.get(2).unwrap().as_str().parse().unwrap();
        solution += num1 * num2;

        // println!("Found capture: {:?}", capture);
        // println!("Number 1: {num1}");
        // println!("Number 2: {num2}");
        // println!("Product: {solution2}");
        // break;
    }

    solution
}
fn main() -> Result<(), Box<dyn Error>> {
    let fpath = "src/data.txt";
    let file_reader = create_file_reader(fpath).expect("Expected a BufReader");

    let mul_pattern = Regex::new(r"mul\((\d+),(\d+)\)").unwrap();

    // Remove any substrings starting with don't and ending with do()
    // After removing these portions, everything else is matched by mul_pattern again
    let cleaning_pattern = Regex::new(r"don't\(\).+?do\(\)").unwrap();

    let mut solution1: isize = 0;
    let mut solution2: isize = 0;

    // read all lines into a single string to have the complete program
    let mut whole_program = String::new();
    for line in file_reader.lines() {
        match line {
            Ok(content) => whole_program.push_str(&content),
            Err(e) => eprintln!("Failed to read a line {}", e),
        }
    }
    solution1 += find_capture_products(&mul_pattern, &whole_program);

    // Remove substrings of the form "don't()....do()"
    // before passing it to find_capture_products
    let cleaned_content = cleaning_pattern.replace_all(&whole_program, "");
    solution2 += find_capture_products(&mul_pattern, &cleaned_content);

    println!("Solution 1: {solution1}");
    println!("Solution 2: {solution2}");
    Ok(())
}

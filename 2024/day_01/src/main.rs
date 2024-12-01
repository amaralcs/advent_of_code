use std::error::Error;
use std::fs::File;
use std::io::{self, BufRead};
// use std::path::Path;

fn parse_line(line_split: &Vec<&str>, idx: usize) -> usize {
    line_split
        .get(idx)
        .unwrap()
        .parse()
        .expect("Error reading idx {idx}")
}

fn main() -> Result<(), Box<dyn Error>> {
    let fpath = "src/data.txt";
    let file = File::open(fpath)?;
    let file_reader = io::BufReader::new(file);

    let mut list_a: Vec<usize> = Vec::new();
    let mut list_b: Vec<usize> = Vec::new();

    for line in file_reader.lines() {
        let line = line?;
        let line_split: Vec<&str> = line.split("   ").collect();

        let item_a: usize = parse_line(&line_split, 0);
        list_a.push(item_a);

        let item_b: usize = parse_line(&line_split, 1);
        list_b.push(item_b);

        // println!("{line_split:?}");
        // println!("List A: {list_a:?}");
        // println!("List B: {list_b:?}");
    }
    assert_eq!(list_a.len(), list_b.len());
    list_a.sort();
    list_b.sort();

    let distances: usize = list_a
        .iter()
        .zip(list_b.iter())
        .map(|(a, b)| a.abs_diff(*b))
        .sum();

    println!("Sum of distances: {distances:?}");

    Ok(())
}

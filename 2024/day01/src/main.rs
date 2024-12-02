use std::collections::HashMap;
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
    let mut freq_a: HashMap<usize, usize> = HashMap::new();
    let mut freq_b: HashMap<usize, usize> = HashMap::new();

    for line in file_reader.lines() {
        let line = line?;
        let line_split: Vec<&str> = line.split("   ").collect();

        let item_a: usize = parse_line(&line_split, 0);
        list_a.push(item_a);
        freq_a.entry(item_a).and_modify(|v| *v += 1).or_insert(1);

        let item_b: usize = parse_line(&line_split, 1);
        list_b.push(item_b);
        freq_b.entry(item_b).and_modify(|v| *v += 1).or_insert(1);

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

    println!("Part 1 solution: {distances}");

    let mut similarity_score: usize = 0;
    for (key, f_a) in freq_a {
        let f_b: &usize = freq_b.get(&key).unwrap_or(&0);
        similarity_score += key * f_a * f_b
    }
    println!("Part 2 solution: {similarity_score}");

    Ok(())
}

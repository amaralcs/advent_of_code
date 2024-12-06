use regex::Regex;
use std::error::Error;
use std::{fs::read_to_string, fs::File, io::BufRead, io::BufReader};

fn create_file_reader(fpath: &str) -> Result<BufReader<File>, Box<dyn Error>> {
    let file = File::open(fpath)?;

    Ok(BufReader::new(file))
}

fn read_file_as_vec(fpath: &str) -> Vec<Vec<String>> {
    let file_reader = BufReader::new(File::open(fpath).unwrap());

    file_reader
        .lines()
        .map(|line| {
            line.expect("Failed to read line")
                .split("")
                .filter(|x| x != &"")
                .map(String::from)
                .collect()
        })
        .collect()
}

fn join_rows(matrix: &Vec<Vec<String>>) -> Vec<String> {
    matrix
        .iter()
        .map(|row| row.iter().as_slice().join(""))
        .collect::<Vec<String>>()
}

fn create_empty_like<T>(matrix: &Vec<Vec<T>>) -> Vec<Vec<T>>
where
    T: Default + Clone, // T must implement Default and Clone
{
    matrix
        .iter()
        .map(|row| vec![T::default(); row.len()]) // Create an empty row of the same length
        .collect()
}

fn rotate_matrix(matrix: &mut Vec<Vec<String>>) -> Vec<Vec<String>> {
    let mut rotated = create_empty_like(matrix);

    for (row_id, row) in matrix.iter_mut().enumerate() {
        for (col_id, rot_row) in rotated.iter_mut().enumerate() {
            row.reverse();
            rot_row[row_id] = row.get(col_id).unwrap().to_string();
            row.reverse(); // unreverse the row so we don't damage the original matrix
        }
    }
    rotated
}

fn row_word_search(matrix: &Vec<Vec<String>>) -> usize {
    // let mut counter = 0;
    let pattern = Regex::new(r"(XMAS|SAMX)").unwrap();

    join_rows(matrix)
        .iter()
        .map(|s| pattern.find_iter(s).count())
        .sum()
}

fn print_matrix(matrix: &Vec<Vec<String>>) {
    println!("");
    for row in matrix {
        println!("{row:?}")
    }
}

fn main() -> Result<(), Box<dyn Error>> {
    let fpath = "src/test.txt";
    let mut contents = read_file_as_vec(fpath);
    let mut solution1 = row_word_search(&contents);
    print_matrix(&contents);
    println!("Solution 1: {}", solution1);

    for i in 0..3 {
        contents = rotate_matrix(&mut contents);
        print_matrix(&contents);
        solution1 += row_word_search(&&contents);
        println!("Solution 1: {}", solution1);
    }

    println!("Solution 1: {}", solution1);

    // let joined = join_rows(&contents);

    // let tmp = contents.split("\\n").collect::<Vec<_>>();
    // let mut tmp = contents.lines().next().unwrap();
    // let tmp = tmp.next();
    // println!("");
    // println!("{tmp:?}");

    Ok(())
}

use itertools::Itertools;
use std::{error::Error, fs::File, io::BufRead, io::BufReader};

fn create_file_reader(fpath: &str) -> Result<BufReader<File>, Box<dyn Error>> {
    let file = File::open(fpath)?;

    Ok(BufReader::new(file))
}

fn run_sign_checks(inputs: &Vec<isize>) -> Vec<bool> {
    inputs
        .iter()
        .tuple_windows()
        .map(|(x, y)| (x.signum() == y.signum()))
        .collect()
}

fn run_magnitude_checks(inputs: &Vec<isize>) -> Vec<bool> {
    inputs
        .iter()
        .map(|x| (x.abs() >= 1) & (x.abs() <= 3))
        .collect()
}

fn run_safety_check(inputs: &Vec<isize>) -> bool {
    let sign_checks: Vec<bool> = run_sign_checks(&inputs);
    let magnitude_checks: Vec<bool> = run_magnitude_checks(&inputs);

    sign_checks.iter().all(|x| *x == true) & magnitude_checks.iter().all(|x| *x == true)
}

fn evaluate_levels(report: &Vec<isize>) -> Vec<isize> {
    report.iter().tuple_windows().map(|(x, y)| x - y).collect()
}

fn parse_report(line: String) -> Vec<isize> {
    line.split_ascii_whitespace()
        .map(|s| {
            s.trim()
                .parse::<isize>()
                .expect("Expected lines to be valid numbers")
        })
        .collect()
}

fn dampen_level(report: &Vec<isize>) -> bool {
    for idx in 0..=report.len() - 1 {
        let mut dampened_report = report.clone();
        dampened_report.remove(idx);

        let cumsum = evaluate_levels(&dampened_report);
        let safety_check = run_safety_check(&cumsum);

        match safety_check {
            true => return true,
            false => continue,
        }
    }

    false
}

fn problem_1(file_reader: BufReader<File>) -> Result<(), Box<dyn Error>> {
    let mut safe_count: usize = 0;

    for (_idx, line) in file_reader.lines().enumerate() {
        let line = line?;
        let report: Vec<isize> = parse_report(line);
        let cumsum: Vec<isize> = evaluate_levels(&report);

        let safety_check = run_safety_check(&cumsum);

        match safety_check {
            true => {
                safe_count += 1;
            }
            false => (),
        }
    }
    println!("Solution 1: There are {safe_count} safe reports");
    Ok(())
}

fn problem_2(file_reader: BufReader<File>) -> Result<(), Box<dyn Error>> {
    let mut safe_count: usize = 0;

    for (_idx, line) in file_reader.lines().enumerate() {
        let line = line?;
        let report: Vec<isize> = parse_report(line);
        let cumsum: Vec<isize> = evaluate_levels(&report);

        let safety_check = run_safety_check(&cumsum);

        match safety_check {
            true => {
                safe_count += 1;
            }
            false => match dampen_level(&report) {
                true => safe_count += 1,
                false => (),
            },
        }
    }
    println!("Solution 2: There are {safe_count} safe reports");
    Ok(())
}

fn main() -> Result<(), Box<dyn Error>> {
    let fpath = "src/data.txt";
    let file_reader = create_file_reader(fpath).expect("Expected a BufReader");
    let _ = problem_1(file_reader);

    let file_reader = create_file_reader(fpath).expect("Expected a BufReader");
    let _ = problem_2(file_reader);

    Ok(())
}

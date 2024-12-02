use std::{error::Error, fs::File, io::BufRead, io::BufReader};

fn create_file_reader(fpath: &str) -> Result<BufReader<File>, Box<dyn Error>> {
    let file = File::open(fpath)?;

    Ok(BufReader::new(file))
}

fn main() -> Result<(), Box<dyn Error>> {
    let fpath = "src/data.txt";
    let file_reader = create_file_reader(fpath).expect("Expected a BufReader");

    for line in file_reader.lines() {
        let line = line?;
        let report = line.split_ascii_whitespace().map(|s| {
            s.trim()
                .parse::<usize>()
                .expect("Expected lines to be valid numbers")
        });
    }

    Ok(())
}

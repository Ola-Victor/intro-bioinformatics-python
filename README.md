Low-Resource Bioinformatics Workflows.

Project Overview:

This project focuses on the design and implementation of lightweight bioinformatics workflows for genomic sequence analysis in resource-limited settings, particularly within the African research and educational context.

Due to limited access to high-performance computing infrastructure in many low- and middle-income countries, many students and early-career researchers are unable to actively engage in bioinformatics research.

This project demonstrates how basic but meaningful bioinformatics analyses can be performed using minimal computational resources, including mobile devices.

Project Objectives.

To develop phone-friendly and low-memory Python scripts for genomic data analysis.

To demonstrate that bioinformatics skills can be acquired and practiced under computational constraints.

To support capacity building in bioinformatics education for African students.

To promote accessible and reproducible research workflows.


Tools & Technologies

1. Python

2. Pandas

3. Matplotlib

4. Pydroid 3 (Android Python IDE)


NOTE: All scripts in this repository were developed and tested on Android using Pydroid 3, without access to high-performance computing resources.


Repository Structure

low_resource_bioinformatics/
│
├── data/
│   └── sample_sequences.csv / fasta files
│
├── scripts/
│   ├── gc_content.py
│   ├── file_based_analysis.py
│   └── visualization.py
│
├── visualizations/
│   └── gc_content_plot.png
│
├── requirements.txt
└── README.md


Analyses Included

1. GC Content Analysis:

Calculates the GC percentage of nucleotide sequences.

Useful for understanding genome composition and stability.


2. File-Based Sequence Analysis:

Reads and processes sequence data directly from files.

Designed to minimize memory usage.

Suitable for large files on low-resource systems.


3. Data Visualization

Simple visual representations of genomic features

Lightweight plots compatible with limited hardware.


Relevance to Africa & Low-Resource Settings

Many African institutions face challenges such as:

Limited access to high-performance computing.

Inadequate bioinformatics infrastructure.

Shortage of practical training opportunities.


This project demonstrates that meaningful bioinformatics learning and analysis is still possible using:

Minimal hardware

Open-source tools

Simplified workflows


It aligns with capacity-building efforts aimed at reducing the computational barrier to bioinformatics education and research in Africa.



How to Run

1. Install Python and required libraries:


pip install pandas matplotlib

2. Clone the repository:


git clone https://github.com/your-username/low_resource_bioinformatics.git

3. Run any script:


python scripts/gc_content.py


Future Directions

1. Extension to FASTA-based workflows

2. Application to disease-related datasets (e.g., cancer genomics)

3. Educational use through mentorship and training programs

4. Integration into STEMIA Project & Research Assistance Scheme


Author

Olalekan Tajudeen H [Ola Victor]
Final-year Biochemistry student, University of Ibadan.
Director, STEMIA Project & Research Assistance Scheme
Aspiring Bioinformatics Researcher

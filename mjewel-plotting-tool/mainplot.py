import argparse
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("file")  # "data/fitnotes_example.csv"
    parser.add_argument("--exercise")  # "Barbell Squat"
    args = parser.parse_args()

    if args.exercise is not None:

        try:
            fitdata = pd.read_csv(args.file)
        except FileNotFoundError:
            print(f"\nERROR: Input file '{args.file}' does not exist\n")
            raise
        
        assert (
            "Exercise" in fitdata.columns
            and "Weight (kgs)" in fitdata.columns
            and "Reps" in fitdata.columns
        )

        exercisedata = fitdata.loc[fitdata["Exercise"] == args.exercise]
        if len(exercisedata) == 0:
            print(f"\nERROR: Exercise '{args.exercise}' is not found in input file\n")
            raise

        x = exercisedata["Reps"]
        y = exercisedata["Weight (kgs)"]

        fig, ax = plt.subplots()
        ax.scatter(x, y)
        ax.set_xlabel("Reps")
        ax.set_ylabel("Weight (kgs)")
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.show()

    else:
        pass


if __name__ == "__main__":
    main()

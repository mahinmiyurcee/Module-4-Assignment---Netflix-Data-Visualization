# Install and load required packages
if (!requireNamespace("ggplot2", quietly = TRUE)) install.packages("ggplot2")
library(ggplot2)

# Read the CSV file
df <- tryCatch(
{
read.csv("C:/Users/Dell/Downloads/Netflix_shows_movies.csv")
  },
  error = function(e) {
    print(paste("Error reading file:", e))
    return(NULL)
  }
)

if (!is.null(df)) {
  # Print the first few rows and structure for debugging
  print(head(df))
  print(str(df))
  # Create the ratings distribution plot
  p <- ggplot(df, aes(x = rating)) +
    geom_bar() +
    theme_minimal() +
    labs(title = "Distribution of Ratings",
         x = "Rating",
         y = "Count") +
    theme(axis.text.x = element_text(angle = 45, hjust = 1))
  # Save the plot
  ggsave("ratings_distribution_r.png", plot = p, width = 10, height = 6)
  print("Plot has been saved as ratings_distribution_r.png")
} else {
  print("Unable to proceed due to error in reading the file.")
}
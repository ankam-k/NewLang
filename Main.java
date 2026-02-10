class Movie {
    String movieName;
    String actorName;
    String actressName;
    String director;
    String production;

    public Movie(String movieName, String actorName, String actressName, String director, String production) {
        this.movieName = movieName;
        this.actorName = actorName;
        this.actressName = actressName;
        this.director = director;
        this.production = production;
    }

    public String getReview() {
        return "Good story and praised for performances.";
    }

    public String getDetails() {
        return "Movie: " + movieName + "\n" +
               "Actor: " + actorName + "\n" +
               "Actress: " + actressName + "\n" +
               "Director: " + director + "\n" +
               "Production: " + production;
    }
}

class PrintDetails {
    public static void printMovieDetails(Movie movie) {
        System.out.println("Telugu Cinema Details:");
        System.out.println(movie.getDetails());
        System.out.println("Review: " + movie.getReview());
        System.out.println();
    }
}

public class Main {
    public static void main(String[] args) {
        Movie movie1 = new Movie("Sareinodu", "Bold Hero", "Nati Shon", "Chandrale", "Sankalp Arts");
        Movie movie2 = new Movie("Poyinadi", "Akkineni Nagarjuna", "Sarojini", "Ajay Chandra", "Ajay Movies");
        Movie movie3 = new Movie("Aranyamu", "Krish", "Anushka", "Gowtham Tinnanuru", "Gowtham Films");

        Movie[] movies = {movie1, movie2, movie3};

        for (Movie movie : movies) {
            PrintDetails.printMovieDetails(movie);
        }
    }
}

/*  
--------------LINEAR SEARCH--------------------

public class Main {
    public int linearSearch(int[] arr, int index, int target){
        if(index==-1){
            System.out.println("Target not found!");
            return -1;
        }
        if(target==arr[index]){
            System.out.print("Target index : ");
            return index;
        }
        return linearSearch(arr, index-1, target);
    }
    public static void main(String[] args){
        Main m= new Main();
        int[] array={1,2,3,4,5,6};
        int target=7;
        int index=array.length-1;
        System.out.print(m.linearSearch(array,index, target));
    }
}


-------------------BINARY SEARCH--------------------

class Main {
    public int binarySearch(int arr[], int start, int end, int target) {
        if (start > end) {
            return -1;
        }
        int mid = (start + end) / 2;
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            return binarySearch(arr, mid + 1, end, target);
        } else {
            return binarySearch(arr, start, mid - 1, target);
        }
    }
    public static void main(String[] args) {
        Main m = new Main();
        int[] array = {1, 2, 3, 4, 5, 6};
        int end = array.length - 1;
        int target = 4;
        int resultIndex = m.binarySearch(array, 0, end, target);
        if (resultIndex != -1) {
            System.out.println("Target " + target + " found at index: " + resultIndex);
        } else {
            System.out.println("Target " + target + " not found in the array.");
        }
    }
}


---------------------without recursion--------------------

class Main {
    public int binarySearch(int arr[], int start, int end, int target) {
        while (start <= end) {
            int mid = (start + end) / 2;
            if (arr[mid] == target) {
                return mid;
            } else if (arr[mid] < target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return -1;
    }
    public static void main(String[] args) {
        Main m = new Main();
        int[] array = {1, 2, 3, 4, 5, 6};
        int end = array.length - 1;
        int target = 4;
        int resultIndex = m.binarySearch(array, 0, end, target);
        if (resultIndex != -1) {
            System.out.println("Target " + target + " found at index: " + resultIndex);
        } else {
            System.out.println("Target " + target + " not found in the array.");
        }
    }
}




 */
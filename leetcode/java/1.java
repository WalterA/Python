
import java.util.ArrayList;
import java.util.List;

class Solution {

    public int[] twoSum(int[] nums, int target) {
        // Convertire l array in una lista per utilizzare il metodo pop

        List<Integer> numList = new ArrayList<>();

        for (int num : nums) {
            numList.add(num);
        }

        // Chiamata alla funzione ricorsiva
        int[] result = ric(numList, target);
        return result;
    }

    private int[] ric(List<Integer> nums, int target) {
        // Se la lista è vuota, restituisce null
        if (nums.isEmpty()) {
            return null;
        }

        // Rimuovere l'ultimo elemento dalla lista
        int ele = nums.remove(nums.size() - 1);

        // Iterare su ciò che rimane nella lista
        for (int i = 0; i < nums.size(); i++) {
            // Controllare se la somma dell'elemento corrente e l'ultimo elemento rimosso è uguale al target
            if (nums.get(i) + ele == target) {
                return new int[]{i, nums.size()}; // Restituisce gli indici
            }
        }

        // Chiamata ricorsiva
        return ric(nums, target);
    }

}

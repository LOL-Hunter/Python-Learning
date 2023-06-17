package de.hunter.Listeners;

import de.hunter.Managers.AllItemsManager;
import org.bukkit.Material;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.inventory.InventoryClickEvent;
import org.bukkit.inventory.Inventory;
import org.bukkit.inventory.ItemStack;

public class on_playerInventoryClickEvent implements Listener {

    @EventHandler
    public static void onEvent(InventoryClickEvent e){
        Player p = (Player) e.getWhoClicked();

        if (p.getOpenInventory().getTitle().startsWith("View")){
            e.setCancelled(true);
            int page = Integer.parseInt(p.getOpenInventory().getTitle().split("_")[1]);
            if (e.getCurrentItem() == null) return;
            if (!e.getCurrentItem().hasItemMeta()) return;
            if (!e.getCurrentItem().getItemMeta().hasDisplayName()) return;

            if (e.getCurrentItem().getItemMeta().getDisplayName().equals("§cBack")){
                if (page == 0) return;
                changeInventory(e.getInventory(), page-1);
            } else if (e.getCurrentItem().getItemMeta().getDisplayName().equals("§aForward")){
                changeInventory(e.getInventory(), page+1);
            }
        }
    }
    public static void changeInventory(Inventory inv, int page){
        int slots = 45;
        if (AllItemsManager.submitted.get(slots*page) == null) return;
        //set title
        for (int i=0; i<=slots-1; i++){
            Material m = AllItemsManager.submitted.get(i+(slots*page));
            if (m == null) continue;
            inv.setItem(i, new ItemStack(m));
        }

    }
}

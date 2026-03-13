#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Team:
    def __init__(self):
        self.records = {}

    def add_team_record(self, tid, captain, batsman, bowlers, allrounders):
        self.records[tid] = {
            "captain": captain,
            "batsman": batsman,
            "bowlers": bowlers,
            "allrounders": allrounders,
            "status": "Active",
            "matches": [] 
        }


class MatchRecord(Team):
    def __init__(self):
        super().__init__()

   
    def add_match_record(self, tid, opponent, runs, result, date):
        if tid in self.records:
            new_match = {
                "opponent": opponent,
                "runs": runs,
                "result": result,
                "date": date
            }
            self.records[tid]["matches"].append(new_match)
            print(f"Match against {opponent} recorded successfully.")
        else:
            print(f"Error: Team ID {tid} not found.")


class Player:
    def __init__(self):
        self.players = {}

    def add_player_record(self, pid, name, team_name):
        self.players[pid] = {"name": name, "team": team_name}


class TournamentSystem:
    def __init__(self):
        self.manager = MatchRecord()
        self.p_manager = Player()

    def menu(self):
        while True:
            print("\n--- TOURNAMENT SYSTEM ---")
            print("1. Add Team")
            print("2. Add Match Record")
            print("3. Update Team Status")
            print("4. Search Team")
            print("5. Display Match Records")
            print("6. Add Player")
            print("7. Display Players")
            print("8. Exit")

            try:
                choice = int(input("Enter choice: "))

                if choice == 1:
                    tid = int(input("Enter Team ID: "))
                    cap = input("Enter Captain Name: ")
                    bt = input("No. of Batsmen: ")
                    bw = input("No. of Bowlers: ")
                    ar = input("No. of Allrounders: ")
                    self.manager.add_team_record(tid, cap, bt, bw, ar)
                    print("Team added successfully.")

                elif choice == 2:
                    tid = int(input("Enter Team ID: "))
                    opp = input("Enter Opponent Team Name: ")
                    runs = input("Enter Runs Scored: ")
                    res = input("Enter Match Result (Win/Loss): ")
                    dt = input("Enter Match Date (DD/MM/YYYY): ")
                    self.manager.add_match_record(tid, opp, runs, res, dt)

                elif choice == 3:
                    tid = int(input("Enter Team ID: "))
                    if tid in self.manager.records:
                        stat = input("Enter new status (Active/Inactive): ")
                        self.manager.records[tid]["status"] = stat
                        print("Status updated.")
                    else: print("Team not found.")

                elif choice == 4:
                    tid = int(input("Enter Team ID to search: "))
                    if tid in self.manager.records:
                        t = self.manager.records[tid]
                        print(f"\n[Team {tid} Details]")
                        print(f"Captain: {t['captain']} | Status: {t['status']}")
                        print(f"Squad: {t['batsman']} Bat, {t['bowlers']} Bowl, {t['allrounders']} All")
                    else: print("Team not found.")

                elif choice == 5:
                    print("\n--- MATCH HISTORY ---")
                    if not self.manager.records:
                        print("No records available.")
                    else:
                        for tid, data in self.manager.records.items():
                            print(f"\nTeam: {data['captain']} (ID: {tid})")
                            if not data["matches"]:
                                print("  No matches recorded.")
                            else:
                                for m in data["matches"]:
                                    print(f"  - VS {m['opponent']} | Runs: {m['runs']} | Result: {m['result']} | Date: {m['date']}")

                elif choice == 6:
                    pid = int(input("Enter Player ID: "))
                    pnm = input("Enter Player Name: ")
                    ptm = input("Enter Team Name: ")
                    self.p_manager.add_player_record(pid, pnm, ptm)
                    print("Player registered.")

                elif choice == 7:
                    print("\n--- REGISTERED PLAYERS ---")
                    if not self.p_manager.players:
                        print("No players found.")
                    for pid, p in self.p_manager.players.items():
                        print(f"ID: {pid} | Name: {p['name']} | Team: {p['team']}")

                elif choice == 8:
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice.")

            except ValueError:
                print("Error: Input must be a number.")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    app = TournamentSystem()
    app.menu()


# In[ ]:





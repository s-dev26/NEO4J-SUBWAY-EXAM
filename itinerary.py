from neo4j import GraphDatabase

class Itinerary:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def find_shortest_path(self, start_x, start_y, end_x, end_y):
        with self.driver.session() as session:
            result = session.run("""
            MATCH (start:Station), (end:Station)
            WHERE start.x = $start_x AND start.y = $start_y 
              AND end.x = $end_x AND end.y = $end_y
            MATCH p = shortestPath((start)-[:LIAISON*]->(end))
            RETURN p
            """, start_x=start_x, start_y=start_y, end_x=end_x, end_y=end_y)

            path = result.single()
            if path:
                return path['p']
            else:
                return None

if __name__ == "__main__":
    itinerary = Itinerary("bolt://localhost:7687", "neo4j", "password")  
    
    start_coords = (652809.2865, 6863002.4359)
    end_coords = (652500, 6863000)
    path = itinerary.find_shortest_path(*start_coords, *end_coords) 

    if path:
        print("Chemin trouvé :", path)
    else:
        print("Aucun chemin trouvé.")
    
    itinerary.close()

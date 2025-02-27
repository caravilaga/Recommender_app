from flask import Flask, request, render_template
from flask_restful import Resource, Api
import pickle
from flask_cors import CORS
import pandas as pd
import numpy as np

## Importar archivos




app = Flask(__name__, template_folder="templates")

CORS(app)
# Crear un objeto API
api = Api(app)

@app.route('/')
def home():
    return render_template('Index.html')

# Objeto predicción del modelo
class prediccion(Resource):
    def get(self,person_id):
        print(person_id)
        person_id = int(person_id)

        # Datos
        products_df = pd.read_csv(r"Datos/products.csv", sep=";")

        # Matriz similitudes
        cosine_sim = np.load("Resultados/sim.npy")

        # Modelo
        with open('Resultados/model.pkl', 'rb') as f:
                    svd = pickle.load(f)

        # Definir la función para el modelo híbrido
        def hybrid_recommendation(user_id, top_n=5):
            all_product_ids = products_df['product_id'].values
            collaborative_scores = []

            for product_id in all_product_ids:
                prediction = svd.predict(user_id, product_id)
                collaborative_scores.append((product_id, prediction.est))
                
                collaborative_scores.sort(key=lambda x: x[1], reverse=True)
                top_collab_products = [x[0] for x in collaborative_scores[:top_n]]

            content_scores = []
            for product_id in top_collab_products:
                idx = products_df[products_df['product_id'] == product_id].index[0]
                sim_scores = list(enumerate(cosine_sim[idx]))
                sorted_sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
                content_scores.append((product_id, sorted_sim_scores[1][1]))  # Take top similar item

                content_scores.sort(key=lambda x: x[1], reverse=True)
                top_content_products = [x[0] for x in content_scores[:top_n]]

            final_recommendations = []
            for product_id in set(top_collab_products + top_content_products):
                collaborative_score = next((score for pid, score in collaborative_scores if pid == product_id), 0)
                content_score = next((score for pid, score in content_scores if pid == product_id), 0)
                final_recommendations.append((product_id, (collaborative_score + content_score) / 2))

                final_recommendations.sort(key=lambda x: x[1], reverse=True)

            return final_recommendations[:top_n]

        prediccion = hybrid_recommendation(person_id, top_n=5)
        recomendacion_id = [x[0] for x in prediccion]
        
        productos = pd.DataFrame(products_df.loc[products_df['product_id'].isin(recomendacion_id),["name","category","descripcion"]])
        productos_res = productos.to_json(orient="records")
        return productos_res   

api.add_resource(prediccion, '/prediccion/<int:person_id>')


if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=8080,debug=True)
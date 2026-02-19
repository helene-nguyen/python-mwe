"""
Centralize storage and management system used primarily in machine learning and software development
to keep track of various model implementations or instances

Key points about a model registry:
- It provides a single place to register and retrieve model classes or instances.
- It enables dynamic instantiation of models based on identifiers, removing tight coupling in code.
- Useful in machine learning pipelines where multiple architectures or versions need to be managed and switched seamlessly.
- Facilitates flexibility, modularity, and ease of experimentation.

See SDK connector Flavien
"""

class ModelRegistry:
    """
    Model classes are registered with a string key via the @ModelRegistry.register('name') decorator.
    You can retrieve and instantiate any registered model dynamically by name with ModelRegistry.get_model(name).
    This pattern helps build extensible machine learning pipelines where you can add
    or switch models without changing client code.
    """
    _models = {}

    @classmethod
    def register(cls, name):
        def decorator(model_cls):
            cls._models[name] = model_cls
            return model_cls
        return decorator

    @classmethod
    def get_model(cls, name):
        model_cls = cls._models.get(name)
        if not model_cls:
            raise ValueError(f"Model '{name}' is not registered.")
        return model_cls

# Example model classes registered automatically
@ModelRegistry.register('linear_regression')
class LinearRegressionModel:
    def train(self):
        return "Training Linear Regression model"

@ModelRegistry.register('decision_tree')
class DecisionTreeModel:
    def train(self):
        return "Training Decision Tree model"

# Usage: create an instance of a model dynamically by its name
model_name = 'decision_tree'
ModelClass = ModelRegistry.get_model(model_name)
model = ModelClass()
print(model.train())  # Output: Training Decision Tree model


# Without decorator
class Registry:
    _reg = {}

    @classmethod
    def register(cls, key, obj):
        cls._reg[key] = obj

    @classmethod
    def get(cls, key):
        return cls._reg.get(key)

# Exemple de classes à enregistrer
class Voiture:
    def rouler(self):
        return "Je roule"

class Moto:
    def rouler(self):
        return "Je roule aussi"

# Enregistrement dans le registre
Registry.register('voiture', Voiture)
Registry.register('moto', Moto)

# Récupération et création dynamiques
vehicule_cls = Registry.get('voiture')
vehicule = vehicule_cls()
print(vehicule.rouler())  # Affiche : Je roule
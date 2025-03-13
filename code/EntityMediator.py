from code.Enemy import Enemy
from code.Entity import Entity


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity): #metodo privado que só funciona dentro da class
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0


    @staticmethod
    def verify_collision(entity_list: list[Entity]): #criando entidades
        for i in range(len(entity_list)): #iterando entidades
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity) #novo metodo

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
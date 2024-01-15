from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category:Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topics: Topic):
        if topics not in self.topics:
            self.topics.append(topics)

    def add_document(self, documents: Document):
        if documents not in self.documents:
            self.documents.append(documents)

    def edit_category(self, category_id: int, new_name:str):
        category = [x for x in self.categories if x.id == category_id][0]
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = [x for x in self.topics if x.id == topic_id][0]
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = [x for x in self.documents if x.id == document_id][0]
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = [x for x in self.categories if x.id == category_id][0]
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = [x for x in self.topics if x.id == topic_id][0]
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = [x for x in self.documents if x.id == document_id][0]
        self.documents.remove(document)

    def get_document(self, document_id):
        document = [x for x in self.documents if x.id == document_id][0]
        return str(document)

    def __repr__(self):
        result = []
        for document in self.documents:
            result.append(str(document))
        return "\n".join(result)




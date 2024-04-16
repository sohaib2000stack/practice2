from transformers import BlenderbotForConditionalGeneration, BlenderbotTokenizer
from fastapi import APIRouter

router = APIRouter()

@router.get("/chatbot/")
async def run_chatbot(user_input: str):
    # Load the model and tokenizer
    model_name = "facebook/blenderbot-400M-distill"
    model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
    tokenizer = BlenderbotTokenizer.from_pretrained(model_name)

    # Generate response
    input_ids = tokenizer(user_input, return_tensors="pt").input_ids
    response_ids = model.generate(input_ids)[0]
    response = tokenizer.decode(response_ids, skip_special_tokens=True)

    return {"response": response}






















# from transformers import BlenderbotForConditionalGeneration, BlenderbotTokenizer
# from fastapi import APIRouter

# router = APIRouter()

# def chatbot():
#     # Load the model and tokenizer
#     model_name = "facebook/blenderbot-400M-distill"
#     model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
#     tokenizer = BlenderbotTokenizer.from_pretrained(model_name)

#     while True:
#         # Get user input
#         user_input = input("You: ")

#         # Generate response
#         input_ids = tokenizer(user_input, return_tensors="pt").input_ids
#         response_ids = model.generate(input_ids)[0]
#         response = tokenizer.decode(response_ids, skip_special_tokens=True)

#         # Print response
#         print(f"Bot: {response}")

#         # Check for exit command
#         if user_input.lower() == "exit":
#             break

# # Call the chatbot function
# chatbot()

# @router.get("hello")
# async def chatbot(title:str):
#     return {"message":chatbot(title)}










# from transformers import BlenderbotForConditionalGeneration, BlenderbotTokenizer
# from fastapi import APIRouter

# router = APIRouter()

# # Load the model and tokenizer
# model_name = "facebook/blenderbot-400M-distill"
# model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
# tokenizer = BlenderbotTokenizer.from_pretrained(model_name)

# @router.get("/chatbot/{title}")
# async def chatbot(title: str):
#     # Generate response
#     input_ids = tokenizer(title, return_tensors="pt").input_ids
#     response_ids = model.generate(input_ids)[0]
#     response = tokenizer.decode(response_ids, skip_special_tokens=True)

#     return {"response": response}










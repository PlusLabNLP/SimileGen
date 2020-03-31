from transformers import AutoTokenizer, BartForConditionalGeneration ,BartConfig
c = BartConfig.from_pretrained('bart-large')
c.output_past = True

model_name_or_path = 'bart-large'
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
model = BartForConditionalGeneration.from_pretrained(model_name_or_path, config=c)

text = "Milton scrunched his eyes and moodily turned back to his computer like a"
input_ids = tokenizer.batch_encode_plus([text], return_tensors='pt')['input_ids']

input_ids = tokenizer.batch_encode_plus([text], return_tensors='pt')['input_ids']
output = model.generate(input_ids=input_ids, max_length=5, num_beams=1)
print(tokenizer.decode(output[0]))

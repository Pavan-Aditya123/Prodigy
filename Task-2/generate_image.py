from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
pipe = pipe.to("cuda")  # Use "cpu" if GPU is unavailable

def generate_image(prompt, output_path="output.png", num_inference_steps=50, guidance_scale=7.5):
    """
    Generate an image using Stable Diffusion
    
    Args:
        prompt (str): Text description of the image to generate
        output_path (str): Path where the generated image will be saved
        num_inference_steps (int): Number of denoising steps (higher = better quality but slower)
        guidance_scale (float): How closely the model follows the prompt (higher = more faithful but less creative)
    """
    try:
        # Generate the image
        image = pipe(
            prompt,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale
        ).images[0]
        
        # Save the image
        image.save(output_path)
        print(f"Image successfully generated and saved to {output_path}")
        return True
    except Exception as e:
        print(f"Error generating image: {str(e)}")
        return False

if __name__ == "__main__":
    # Example usage
    prompt = input("Enter your image description: ")
    output_file = input("Enter output filename (default: output.png): ") or "output.png"
    
    generate_image(prompt, output_file)

<template>
  <div
    class="min-h-screen flex flex-col items-center justify-center bg-gradient-to-r from-blue-500 to-purple-600 p-6 text-white"
  >
    <div class="bg-white p-8 rounded-2xl shadow-lg max-w-lg w-full text-center text-gray-900">
      <h1 class="text-3xl font-bold mb-6">AI Image Caption Generator</h1>
      <label
        class="cursor-pointer bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition inline-block mb-4"
      >
        Upload Image
        <input type="file" @change="uploadImage" accept="image/*" class="hidden" />
      </label>
      <div v-if="imageUrl" class="mb-4 border rounded-lg overflow-hidden shadow-lg">
        <img :src="imageUrl" alt="Uploaded" class="w-full max-h-72 object-cover" />
      </div>
      <button
        @click="generateCaption"
        :disabled="loading"
        class="bg-purple-500 text-white px-6 py-2 rounded-lg hover:bg-purple-600 transition w-full"
      >
        {{ loading ? 'Generating...' : 'Generate Caption' }}
      </button>
      <p v-if="caption" class="mt-6 text-xl font-semibold bg-gray-200 p-4 rounded-lg shadow-inner">
        {{ caption }}
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const imageFile = ref(null)
const imageUrl = ref('')
const caption = ref('')
const loading = ref(false)

const uploadImage = (event) => {
  const file = event.target.files[0]
  if (file) {
    imageFile.value = file
    imageUrl.value = URL.createObjectURL(file)
  }
}

const generateCaption = async () => {
  if (!imageFile.value) return
  loading.value = true
  caption.value = ''

  const formData = new FormData()
  formData.append('file', imageFile.value)

  try {
    const response = await axios.post('http://127.0.0.1:8000/generate-caption/', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    })
    caption.value = response.data.caption || 'No caption generated'
  } catch (error) {
    caption.value = 'Error generating caption'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
input[type='file'] {
  display: none;
}
</style>

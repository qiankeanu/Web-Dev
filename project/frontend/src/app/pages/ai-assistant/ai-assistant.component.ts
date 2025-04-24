import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-ai-assistant',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './ai-assistant.component.html'
})
export class AiAssistantComponent {
  message: string = '';
  chatHistory: any[] = [
    {
      role: 'assistant',
      content: 'Привет! Я ваш AI-ассистент по поиску работы. Чем могу помочь?'
    }
  ];
  popularQuestions = [
    'Как составить эффективное резюме?',
    'Какие навыки сейчас востребованы на рынке?',
    'Как подготовиться к техническому собеседованию?',
    'Как вести себя на собеседовании?'
  ];

  capabilities = [
    'Помощь в поиске подходящих вакансий',
    'Анализ и улучшение резюме',
    'Советы по подготовке к собеседованию',
    'Информация о требуемых навыках и технологиях',
    'Персонализированные карьерные рекомендации'
  ];

  constructor(private apiService: ApiService) {}

  sendMessage() {
    if (!this.message.trim()) return;

    // Add user message to chat
    this.chatHistory.push({
      role: 'user',
      content: this.message
    });

    // Call AI API
    this.apiService.sendChatMessage(this.message).subscribe({
      next: (response) => {
        this.chatHistory.push({
          role: 'assistant',
          content: response.message
        });
      },
      error: (error) => {
        console.error('Error sending message:', error);
      }
    });

    this.message = '';
  }

  askQuestion(question: string) {
    this.message = question;
    this.sendMessage();
  }
}
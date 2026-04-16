// Service Worker for offline support

const CACHE_NAME = 'lingqiusheng-stickers-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/stickers_metadata.json'
];

// Install Service Worker
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(urlsToCache).catch(() => {
        // 如果缓存模式添加失败，不中断安装过程
        console.log('一些资源缓存失败');
      });
    })
  );
  self.skipWaiting();
});

// Activate Service Worker
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheName !== CACHE_NAME) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
  self.clients.claim();
});

// Fetch Event - Different strategies for different resources
self.addEventListener('fetch', event => {
  // 只缓存GET请求
  if (event.request.method !== 'GET') {
    return;
  }

  const url = event.request.url;
  
  // 判断资源类型
  const isSticker = url.includes('/stickers/');
  const isHtmlOrMetadata = url.includes('index.html') || url.includes('stickers_metadata.json');

  if (isSticker) {
    // 表情包文件：缓存优先策略
    event.respondWith(cacheFirstStrategy(event.request));
  } else if (isHtmlOrMetadata) {
    // HTML和元数据：网络优先策略
    event.respondWith(networkFirstStrategy(event.request));
  } else {
    // 其他资源：缓存优先策略
    event.respondWith(cacheFirstStrategy(event.request));
  }
});

// 缓存优先策略：先查找缓存，缓存没有则网络请求
function cacheFirstStrategy(request) {
  return caches.match(request).then(response => {
    if (response) {
      return response;
    }

    return fetch(request).then(response => {
      // 检查有效响应
      if (!response || response.status !== 200 || response.type !== 'basic') {
        return response;
      }

      // 缓存响应
      const responseToCache = response.clone();
      caches.open(CACHE_NAME).then(cache => {
        cache.put(request, responseToCache);
      });

      return response;
    }).catch(() => {
      // 离线时返回缓存
      return caches.match(request);
    });
  });
}

// 网络优先策略：先网络请求，网络失败则查找缓存
function networkFirstStrategy(request) {
  return fetch(request).then(response => {
    // 检查有效响应
    if (!response || response.status !== 200 || response.type !== 'basic') {
      return response;
    }

    // 缓存响应
    const responseToCache = response.clone();
    caches.open(CACHE_NAME).then(cache => {
      cache.put(request, responseToCache);
    });

    return response;
  }).catch(() => {
    // 网络请求失败，返回缓存
    return caches.match(request);
  });
}
